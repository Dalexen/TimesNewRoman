import SwiftUI

struct StartView: View {
    @ObservedObject var viewModel: QuizViewModel
    @Binding var hasStarted: Bool
    @State private var selectedCount = 10

    private let options = [10, 20, 50, 100]

    var body: some View {
        VStack(spacing: 28) {
            Spacer()

            GlassCard {
                VStack(spacing: 12) {
                    Text("Times New Roman")
                        .font(.system(size: 34, weight: .semibold, design: .serif))
                        .multilineTextAlignment(.center)
                    Text("A trivia game about the world's most famous typeface, and the history of type itself.")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                }
            }

            GlassCard {
                VStack(alignment: .leading, spacing: 14) {
                    Text("How many questions?")
                        .font(.headline)
                    Picker("Question count", selection: $selectedCount) {
                        ForEach(options, id: \.self) { count in
                            Text("\(count)").tag(count)
                        }
                    }
                    .pickerStyle(.segmented)
                }
            }

            Button {
                viewModel.startNewGame(count: selectedCount)
                hasStarted = true
            } label: {
                Text("Start Quiz")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 6)
            }
            .glassButtonStyleCompat()
            .controlSize(.large)
            .padding(.horizontal)
            .disabled(!viewModel.hasQuestions)

            Spacer()
        }
        .padding()
    }
}

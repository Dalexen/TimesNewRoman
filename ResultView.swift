import SwiftUI

struct ResultView: View {
    @ObservedObject var viewModel: QuizViewModel
    @Binding var hasStarted: Bool

    var body: some View {
        VStack(spacing: 24) {
            Spacer()

            GlassCard {
                VStack(spacing: 12) {
                    Text("SCORE")
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(.secondary)
                    Text("\(viewModel.score) / \(viewModel.questionCount)")
                        .font(.system(size: 48, weight: .bold, design: .serif))
                    Text(message)
                        .multilineTextAlignment(.center)
                        .foregroundStyle(.secondary)
                }
            }

            Button("Play Again") {
                hasStarted = false
            }
            .glassButtonStyleCompat()
            .controlSize(.large)
            .padding(.horizontal)

            Spacer()
        }
        .padding()
    }

    private var message: String {
        let ratio = viewModel.questionCount > 0
            ? Double(viewModel.score) / Double(viewModel.questionCount)
            : 0
        switch ratio {
        case 0.9...: return "Certified typophile."
        case 0.7..<0.9: return "Solid grasp of serifs and history."
        case 0.4..<0.7: return "Getting there — try another round."
        default: return "The Times would like a word."
        }
    }
}

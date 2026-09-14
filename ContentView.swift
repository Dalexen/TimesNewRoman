import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = QuizViewModel()
    @State private var hasStarted = false

    var body: some View {
        NavigationStack {
            ZStack {
                backgroundGradient
                Group {
                    if viewModel.loadError {
                        errorView
                    } else if !hasStarted {
                        StartView(viewModel: viewModel, hasStarted: $hasStarted)
                    } else if viewModel.isFinished {
                        ResultView(viewModel: viewModel, hasStarted: $hasStarted)
                    } else {
                        QuizView(viewModel: viewModel)
                    }
                }
            }
            .navigationTitle("Times New Roman")
            .navigationBarTitleDisplayMode(.inline)
        }
        .onAppear { viewModel.loadQuestions() }
    }

    private var backgroundGradient: some View {
        LinearGradient(
            colors: [Color(red: 0.05, green: 0.05, blue: 0.08), Color(red: 0.14, green: 0.10, blue: 0.20)],
            startPoint: .top,
            endPoint: .bottom
        )
        .ignoresSafeArea()
    }

    private var errorView: some View {
        GlassCard {
            VStack(spacing: 8) {
                Text("Couldn't load questions")
                    .font(.headline)
                Text("The bundled questions.json file is missing or invalid.")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}

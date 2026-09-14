import SwiftUI

struct QuizView: View {
    @ObservedObject var viewModel: QuizViewModel

    var body: some View {
        VStack(spacing: 20) {
            ProgressView(value: viewModel.progress)
                .tint(.white)
                .padding(.horizontal)

            if let question = viewModel.currentQuestion {
                ScrollView {
                    VStack(spacing: 20) {
                        GlassCard {
                            VStack(alignment: .leading, spacing: 10) {
                                Text(question.category.uppercased())
                                    .font(.caption.weight(.semibold))
                                    .foregroundStyle(.secondary)
                                Text(question.prompt)
                                    .font(.title3.weight(.semibold))
                            }
                            .frame(maxWidth: .infinity, alignment: .leading)
                        }

                        VStack(spacing: 12) {
                            ForEach(Array(question.options.enumerated()), id: \.offset) { index, option in
                                Button {
                                    viewModel.selectOption(index)
                                } label: {
                                    HStack {
                                        Text(option)
                                            .multilineTextAlignment(.leading)
                                        Spacer()
                                        if let selected = viewModel.selectedOptionIndex {
                                            if index == question.correctIndex {
                                                Image(systemName: "checkmark.circle.fill")
                                                    .foregroundStyle(.green)
                                            } else if index == selected {
                                                Image(systemName: "xmark.circle.fill")
                                                    .foregroundStyle(.red)
                                            }
                                        }
                                    }
                                    .padding()
                                    .frame(maxWidth: .infinity)
                                }
                                .glassButtonStyleCompat()
                                .disabled(viewModel.selectedOptionIndex != nil)
                            }
                        }
                    }
                    .padding(.horizontal)
                    .padding(.bottom, 100)
                }

                if viewModel.selectedOptionIndex != nil {
                    Button(viewModel.currentIndex + 1 == viewModel.sessionQuestions.count ? "See Results" : "Next Question") {
                        viewModel.nextQuestion()
                    }
                    .glassButtonStyleCompat()
                    .controlSize(.large)
                    .padding(.horizontal)
                    .padding(.bottom)
                }
            }
        }
        .padding(.top)
        .animation(.default, value: viewModel.selectedOptionIndex)
    }
}

import Foundation

struct Question: Identifiable, Codable, Equatable {
    let id: Int
    let category: String
    let prompt: String
    let options: [String]
    let correctIndex: Int
}

@MainActor
final class QuizViewModel: ObservableObject {
    @Published private(set) var allQuestions: [Question] = []
    @Published private(set) var sessionQuestions: [Question] = []
    @Published var currentIndex: Int = 0
    @Published var score: Int = 0
    @Published var selectedOptionIndex: Int? = nil
    @Published var isFinished: Bool = false
    @Published private(set) var questionCount: Int = 10
    @Published var loadError: Bool = false

    var currentQuestion: Question? {
        guard currentIndex >= 0, currentIndex < sessionQuestions.count else { return nil }
        return sessionQuestions[currentIndex]
    }

    var progress: Double {
        guard !sessionQuestions.isEmpty else { return 0 }
        return Double(currentIndex) / Double(sessionQuestions.count)
    }

    var hasQuestions: Bool { !allQuestions.isEmpty }

    func loadQuestions() {
        guard !allQuestions.isEmpty else {
            guard
                let url = Bundle.main.url(forResource: "questions", withExtension: "json"),
                let data = try? Data(contentsOf: url),
                let decoded = try? JSONDecoder().decode([Question].self, from: data)
            else {
                loadError = true
                return
            }
            allQuestions = decoded
            return
        }
    }

    func startNewGame(count: Int) {
        questionCount = min(count, allQuestions.count)
        sessionQuestions = Array(allQuestions.shuffled().prefix(questionCount))
        currentIndex = 0
        score = 0
        selectedOptionIndex = nil
        isFinished = false
    }

    func selectOption(_ index: Int) {
        guard selectedOptionIndex == nil, let question = currentQuestion else { return }
        selectedOptionIndex = index
        if index == question.correctIndex {
            score += 1
        }
    }

    func nextQuestion() {
        selectedOptionIndex = nil
        if currentIndex + 1 < sessionQuestions.count {
            currentIndex += 1
        } else {
            isFinished = true
        }
    }
}

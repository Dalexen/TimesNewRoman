import SwiftUI

/// A card container that uses real iOS 26 "Liquid Glass" (`.glassEffect`) when
/// available, and falls back to a `.ultraThinMaterial` look on iOS 17-25.
struct GlassCard<Content: View>: View {
    var cornerRadius: CGFloat = 24
    @ViewBuilder var content: Content

    var body: some View {
        let shape = RoundedRectangle(cornerRadius: cornerRadius, style: .continuous)
        if #available(iOS 26.0, *) {
            content
                .padding(20)
                .glassEffect(.regular, in: shape)
        } else {
            content
                .padding(20)
                .background(
                    shape
                        .fill(.ultraThinMaterial)
                        .overlay(shape.stroke(Color.white.opacity(0.22), lineWidth: 1))
                )
        }
    }
}

/// Applies the real Liquid Glass button style on iOS 26+, and a sensible
/// bordered-prominent fallback on earlier iOS versions.
struct GlassButtonStyleCompat: ViewModifier {
    func body(content: Content) -> some View {
        if #available(iOS 26.0, *) {
            content.buttonStyle(.glass)
        } else {
            content.buttonStyle(.borderedProminent)
        }
    }
}

extension View {
    func glassButtonStyleCompat() -> some View {
        modifier(GlassButtonStyleCompat())
    }
}

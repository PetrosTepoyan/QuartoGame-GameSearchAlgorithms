//
//  BoardView.swift
//  Quarto-Mobile
//
//  Created by Петрос Тепоян on 12/4/21.
//

import SwiftUI

struct BoardView: View {
    
    let board: [[Int]] = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]]
    
    
    
    var body: some View {
        GeometryReader { geo in
            boardView
                .frame(width: geo.size.width, height: geo.size.width, alignment: .center)
        }
        
    }
    
    var boardView: some View {
        VStack {
            ForEach(0..<4) { i in
                HStack {
                    ForEach(0..<4) { j in
                        let id = board[i][j]
                        PieceView(id: id)
                    }
                }
            }
        }
    }
}

struct BoardView_Previews: PreviewProvider {
    static var previews: some View {
        BoardView()
            .ignoresSafeArea(.all, edges: .all)
            .background(Color.gray)
    }
}

private struct SafeAreaInsetsKey: EnvironmentKey {
    static var defaultValue: EdgeInsets {
        (UIApplication.shared.windows.first(where: { $0.isKeyWindow })?.safeAreaInsets ?? .zero).insets
    }
}

extension EnvironmentValues {
    
    var safeAreaInsets: EdgeInsets {
        self[SafeAreaInsetsKey.self]
    }
}

private extension UIEdgeInsets {
    
    var insets: EdgeInsets {
        EdgeInsets(top: top, leading: left, bottom: bottom, trailing: right)
    }
}

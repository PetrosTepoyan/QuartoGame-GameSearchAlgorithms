//
//  PieceView.swift
//  Quarto-Mobile
//
//  Created by Петрос Тепоян on 12/4/21.
//

import SwiftUI

struct PieceView: View {
    
    let piece: Piece
    
    init(piece: Piece) {
        self.piece = piece
    }
    
    init(id: Int) {
        self.piece = .all[id - 1]
    }
    
    var body: some View {
        shape
            .overlay(hole)
            .scaleEffect(piece.big ? 1 : 0.8)
            .aspectRatio(1, contentMode: .fit)
            .padding(5)
    }
    
    @ViewBuilder
    var hole: some View {
        if piece.holed {
            Circle()
                .fill(Color.gray.opacity(0.5))
                .padding()
        }
    }
    
    @ViewBuilder
    var shape: some View {
        if piece.round {
            Circle()
                .fill(piece.white ? Color.white : Color.black)
        } else {
            Rectangle()
                .fill(piece.white ? Color.white : Color.black)
                .cornerRadius(20)
        }
    }
}

struct PieceView_Previews: PreviewProvider {
    static var previews: some View {
        PieceView(piece: .all[0])
            .background(Color.gray)
    }
}

//
//  PiecePicker.swift
//  Quarto-Mobile
//
//  Created by Петрос Тепоян on 12/4/21.
//

import SwiftUI

struct PiecePicker: View {
    
    let pieces: [Piece] = Piece.all
    
    let drag: DragGesture = .init(minimumDistance: 0, coordinateSpace: .global)
    
    @State var offset: CGSize = .zero
    
    var body: some View {
        ScrollView(.horizontal) {
            HStack {
                ForEach(pieces) { piece in
                    PieceView(piece: piece)
                        .gesture(drag.onChanged { value in
                            offset = value.translation
                        })
                        .offset(x: offset.width, y: offset.height)
                }
            }
        }
    }
}

struct PiecePicker_Previews: PreviewProvider {
    static var previews: some View {
        PiecePicker()
            .frame(width: UIScreen.main.bounds.width,
                   height: 70,
                   alignment: .center)
            .background(Color.gray)
    }
}

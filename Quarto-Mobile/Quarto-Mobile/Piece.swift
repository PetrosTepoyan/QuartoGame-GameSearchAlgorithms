//
//  Piece.swift
//  Quarto-Mobile
//
//  Created by Петрос Тепоян on 12/4/21.
//

import SwiftUI

struct Piece: Identifiable {
    
    let id: UUID = UUID()
    
    let round: Bool
    
    let white: Bool
    
    let big: Bool
    
    let holed: Bool
    
    init(round: Bool, white: Bool, big: Bool, holed: Bool) {
        self.round = round
        self.white = white
        self.big = big
        self.holed = holed
    }
    
    static let all: [Piece] = [
        Piece(round: false, white: false, big: false, holed: false),
        Piece(round: false, white: false, big: false, holed: true),
        Piece(round: false, white: false, big: true,  holed: false),
        Piece(round: false, white: false, big: true,  holed: true),
        Piece(round: false, white: true,  big: false, holed: false),
        Piece(round: false, white: true,  big: false, holed: true),
        Piece(round: false, white: true,  big: true,  holed: false),
        Piece(round: false, white: true,  big: true,  holed: true),
        Piece(round: true,  white: false, big: false, holed: false),
        Piece(round: true,  white: false, big: false, holed: true),
        Piece(round: true,  white: false, big: true,  holed: false),
        Piece(round: true,  white: false, big: true,  holed: true),
        Piece(round: true,  white: true,  big: false, holed: false),
        Piece(round: true,  white: true,  big: false, holed: true),
        Piece(round: true,  white: true,  big: true,  holed: false),
        Piece(round: true,  white: true,  big: true,  holed: true)
    ]
}

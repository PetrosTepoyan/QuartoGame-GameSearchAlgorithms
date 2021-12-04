//
//  MainView.swift
//  Quarto-Mobile
//
//  Created by Петрос Тепоян on 12/4/21.
//

import SwiftUI

struct MainView: View {
    
    @Environment(\.safeAreaInsets) private var safeAreaInsets
    
    var body: some View {
        VStack {
            VStack {
                Text("Board")
                    .foregroundColor(.white)
                    .font(.title.bold())
                
                BoardView()
                    .aspectRatio(1, contentMode: .fit)
                    
            }
            .padding()
            .padding(.top, safeAreaInsets.top)
            
            VStack {
                Text("Available pieces")
                    .foregroundColor(.white)
                    .font(.title.bold())
                
                PiecePicker()
                    .frame(width: UIScreen.main.bounds.width,
                           height: 70,
                           alignment: .center)
            }
            
            Spacer()
        }
        .ignoresSafeArea(.all, edges: .all)
        .background(Color.gray)
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}

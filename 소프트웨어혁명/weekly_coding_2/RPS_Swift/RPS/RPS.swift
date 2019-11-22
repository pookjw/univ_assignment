//
//  RPS.swift
//  RPS
//
//  Created by pook on 11/20/19.
//  Copyright © 2019 pookjw. All rights reserved.
//

import Foundation

class RPS{
    let count: Int
    var player_won_count = 0
    var computer_won_count = 0
    var draw_count = 0
    var played_count: Int {
        player_won_count + computer_won_count + draw_count
    }
    
    init(count: Int) {
        self.count = count
    }
    
    enum Cases: Int{
        case rock, scissor, paper
    }
    
    func play(_ player_case: Cases){
        let computer_case = Cases(rawValue: [0, 1, 2].randomElement()!)!
        let case_array = [player_case.rawValue, computer_case.rawValue].sorted()
        
        func result(win_case: Int? = nil, draw: Bool? = nil){
            // Result Messages
            var result_score: String { "Player: \(player_won_count), Computer: \(computer_won_count), Draw: \(draw_count)" }
            var result_player_win: String { "Game Over! Player win! (\(result_score))" }
            var result_computer_win: String { "Game Over! Computer win! (\(result_score))" }
            var result_draw: String { "Game Over! Draw! (\(result_score))" }
            // End
            
            if played_count == count {
                print("Already played all games!")
            } else {
                if draw == Bool?(true){
                    print("Draw!")
                    draw_count += 1
                } else if computer_case.rawValue == win_case {
                    print("Computer win!")
                    computer_won_count += 1
                } else if player_case.rawValue == win_case {
                    print("Player win!")
                    player_won_count += 1
                }
                
                // If played all games, print result message...
                if played_count == count{
                    if player_won_count > computer_won_count{
                        print(result_player_win)
                    } else if player_won_count < computer_won_count{
                        print(result_computer_win)
                    } else {
                        print(result_draw)
                    }
                }
            }
        }
        
        if case_array[0] == case_array[1] {
            result(draw: true)
        } else if case_array[0] == 0 && case_array[1] == 1{
            result(win_case: 0)
        } else if case_array[0] == 0 && case_array[1] == 2{
            result(win_case: 2)
        } else if case_array[0] == 1 && case_array[1] == 2{
            result(win_case: 1)
        }
    }
}

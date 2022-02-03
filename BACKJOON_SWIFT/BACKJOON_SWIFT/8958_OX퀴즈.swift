//
//  8958_OX퀴즈.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/03.
//

import Foundation




func sol8958(){
    let n = Int(readLine()!)!
    
    for _ in 0..<n{
        
        let ox = readLine()!
        
        var answer = 0
        var count = 1
        ox.forEach { char in
            if char == "O" {
                answer += count
                count += 1
            }
            
            else{
                count = 1
                
            }
        }
        
        print(answer)
        
    }
            
    
}

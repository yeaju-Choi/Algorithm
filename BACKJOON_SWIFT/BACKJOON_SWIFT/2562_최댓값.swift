//
//  2562_최댓값.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/01/31.
//

import Foundation

func sol2562(){
    
    var numbers: [Int] = []
    
    for _ in 0..<9 {
        numbers.append(Int(readLine()!)!)
    }
    let max = numbers.max()!

    print(max)
    print(numbers.firstIndex(of: max)! + 1)
    
    
    
}

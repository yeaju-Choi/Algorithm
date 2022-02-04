//
//  2217_로프.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/05.
//

import Foundation

func sol2217(){
    
    let n = Int(readLine()!)!
    var ropes: [Int] = Array()

    for _ in 0..<n{
        ropes.append(Int(readLine()!)!)
    }
    
    ropes.sort()
    var max = ropes.max()!
    
    
    for i in 0..<ropes.count{
        if ropes[i] * (ropes.count-i) > max {
            max = ropes[i] * (ropes.count-i)
        }
    }
    print(max)
            
            

    
    
    
    
    
    
}

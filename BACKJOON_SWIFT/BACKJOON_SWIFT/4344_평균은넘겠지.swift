//
//  4344_평균은넘겠지.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/03.
//

import Foundation

func average(_ arr: [Int]) -> Double {
    var total = 0
    for i in 1..<arr.count {
        total += arr[i]
    }
    return Double(total)/Double(arr.count-1)
   
}

func averagePercent(){
    let scores = readLine()!.split(separator: " ").map { Int($0)! }
    
    var upperAverage = 0.0
    let average = average(scores)
    
    for i in 1..<scores.count{
        if Double(scores[i]) > average{
            upperAverage += 1
        }
    }
    
    print(String(format: "%.3f", (Double(upperAverage)/Double(scores[0]))*100.0)+"%")
    
}


func sol4344(){
    
    let n = Int(readLine()!)!
    
    for _ in 0..<n{
        averagePercent()
        
    }
    
    
}

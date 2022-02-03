//
//  1546_평균.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/03.
//

import Foundation

func sol1546(){
    
    let n = Int(readLine()!)!
    
    let scores: [Double] = readLine()!.split(separator: " ").map { Double($0)! }
    
    let maxScore = scores.max()!
    
    var total: Double = 0.0
    
    scores.forEach {
        total += Double( ($0/maxScore) * 100.0)
    }
    print(total/Double(n))
    
}

//
//  행렬의덧셈.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/21.
//

import Foundation


func 행렬의덧셈(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
// MARK: zip은 시퀀스 끼리 묶어주는 기능을 함
    return zip(arr1, arr2).map{zip($0, $1).map{$0+$1}}
    
// MARK: Other Answer
//    var answer: [[Int]] = Array(repeating: Array(repeating: 0, count: arr1[0].count), count: arr1.count)
//
//    for i in 0..<arr1.count {
//        for j in 0..<arr1[i].count {
//            answer[i][j] = arr1[i][j] + arr2[i][j]
//        }
//    }
//    return answer
}

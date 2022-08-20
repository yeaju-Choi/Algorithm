//
//  직사각형별찍기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/20.
//

import Foundation

func 직사각형별찍기(){
    
    let n = readLine()!.components(separatedBy: " ").map { Int($0)! }
//    for _ in 0..<n[1] {
//        for _ in 0..<n[0] {
//            print("*", separator: " ", terminator: "")
//        }
//        print("")
//    }
    
    let (a,b) = (n[0],n[1])
    for _ in 0..<b {
        print(Array(repeating: "*", count: a).joined())
    }
    
    
}

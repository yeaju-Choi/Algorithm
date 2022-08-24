//
//  평균구하기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/23.
//

import Foundation

func 평균구하기(_ arr:[Int]) -> Double {
    return arr.reduce(0, {$0 + Double($1)}) / Double(arr.count)
}

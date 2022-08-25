//
//  제일작은수제거하기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/25.
//

import Foundation

func 제일작은수제거하기(_ arr:[Int]) -> [Int] {
    // min() => O(n)
    let min = arr.min()!
    return arr.count == 1 ? [-1] : arr.filter{ $0 > min}
}

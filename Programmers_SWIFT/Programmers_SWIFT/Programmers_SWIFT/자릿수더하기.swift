//
//  자릿수더하기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/27.
//

import Foundation

func 자릿수더하기(_ n:Int) -> Int {
    return String(n).map{Int(String($0))!}.reduce(0,+)
}

//
//  나머지가1이되는수찾기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/10.
//

import Foundation

func 나머지가1이되는수찾기(_ n:Int) -> Int {
    return (2...n).filter{ n % $0 == 1 }.first!
}

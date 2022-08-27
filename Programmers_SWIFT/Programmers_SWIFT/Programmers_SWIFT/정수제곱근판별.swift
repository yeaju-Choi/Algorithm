//
//  정수제곱근판별.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/25.
//

import Foundation

// Int(exactly: ) 사용
func 정수제곱근판별(_ n:Int64) -> Decimal {
    guard let b = Int(exactly: sqrt(Double(n))) else {return -1}
    return pow(Decimal(b+1), 2)
}

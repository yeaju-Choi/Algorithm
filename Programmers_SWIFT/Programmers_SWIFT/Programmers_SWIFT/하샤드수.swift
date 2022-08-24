//
//  하샤드수.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/23.
//

import Foundation

func 하샤드수(_ x:Int) -> Bool {
    // x숫자를 한자리씩 배열로 만든다
    return x % String(x).map{Int(String($0))!}.reduce(0,+) == 0 ? true : false
}

//
//  콜라츠추측.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/23.
//

import Foundation

func 콜라츠추측(_ num:Int) -> Int {
    var copyNum = num
    
    for i in 0..<500 {
        if copyNum == 1 { return i }
        copyNum = copyNum % 2 == 0 ? copyNum / 2 : copyNum * 3 + 1
    }
    return -1
}

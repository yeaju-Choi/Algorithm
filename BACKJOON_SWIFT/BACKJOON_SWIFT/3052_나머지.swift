//
//  3052_나머지.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/03.
//

import Foundation


func sol3052(){
    
    var dict: [Int:Bool] = Dictionary()
    
    for _ in 0...9{
        let num = Int(readLine()!)!
        dict[num % 42] = true
     }
    
    print(dict.keys.count)
        
}

func sol3052_2(){
    
    var r: Set<Int> = []
    for _ in 1...10 {
        r.insert(Int(readLine()!)!%42)
    }
    print(r.count)
}

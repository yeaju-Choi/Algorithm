//
//  10818_최소,최대.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/01/31.
//

import Foundation

func sol10818(){
    
    let _ = Int(readLine()!)!
    let numbers = readLine()!.split(separator: " ").map { Int(String($0))!}
    
    print(numbers.min()!, numbers.max()!)
    
}

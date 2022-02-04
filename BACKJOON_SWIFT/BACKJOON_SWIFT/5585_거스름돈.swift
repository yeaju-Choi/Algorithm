//
//  5585_거스름돈.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/05.
//

import Foundation

func sol5585(){
    
    let moneySet = [500,100,50,10,5,1]
    
    var input = Int(readLine()!)!
    input = 1000 - input
    
    var count = 0
    
    while (input > 0){
        
        
        for yen in moneySet {
            if input % yen == 0{
                input -= yen
                count += 1
                break
            }
        }
        
    }
    print(count)
}

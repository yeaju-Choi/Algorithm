//
//  10773_제로.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/03/02.
//

import Foundation

struct Stack<T> {
    var stack: [T] = []
    var count: Int {
        return stack.count
    }
    
    mutating func push(_ item: T) { stack.append(item)}
    mutating func pop() -> T? {
        return stack.isEmpty ? nil : stack.popLast()
    }
    
}


func sol10773(){
    
    var stack: Stack<Int> = Stack()
    
    let k = Int(readLine()!)!
    for _ in 0..<k {
        let number = Int(readLine()!)!
        if number == 0{
            stack.pop()
        }else { stack.push(number) }
    }
    
    let sum = stack.stack.reduce(0) { n1,n2 in
        return n1+n2
    }
    print(sum)
    
}

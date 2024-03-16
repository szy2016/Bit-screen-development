package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
    "strings"
)

func main() {
    // 打开文件
    file, err := os.Open("example.txt")
    if err != nil {
        log.Fatalf("无法打开文件: %v", err)
    }
    defer file.Close() // 确保在函数结束时关闭文件

    // 创建一个新的Scanner对象
    scanner := bufio.NewScanner(file)

    // 创建一个切片来存储最终的词典列表
    var dictionaries []map[string]interface{}

    // 使用Scanner的Scan方法逐行读取文件
    for scanner.Scan() {
        line := scanner.Text() // 获取当前行的文本
        // 使用strings.Fields按空格分割行内容
        fields := strings.Fields(line)
        if len(fields) >= 2 {
            // 提取第一和第二个值，并创建一个新的词典
            // 假设这两个值是字符串或可以转换为字符串的数字
            firstValue := fields[0]
            secondValue := fields[1]
            // 如果需要，你可以在这里添加错误处理来确保值是有效的
            // 例如，使用strconv.Atoi或strconv.ParseFloat来转换数字

            // 创建词典并将第一和第二个值赋给`use`这个键
            dictionary := make(map[string]interface{})
            dictionary["use"] = map[string]string{
                "first":  firstValue,
                "second": secondValue,
            }

            // 将词典添加到列表中
            dictionaries = append(dictionaries, dictionary)
        } else {
            // 处理行中没有足够字段的情况（如果需要）
            fmt.Printf("行 '%s' 不包含足够的字段\n", line)
        }
    }

    // 检查是否有读取错误
    if err := scanner.Err(); err != nil {
        log.Fatalf("读取文件时发生错误: %v", err)
    }

    // 打印出最终的词典列表
    for _, dictionary := range dictionaries {
        fmt.Println(dictionary)
    }
}

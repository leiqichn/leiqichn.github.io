---
title: leetcode 271.字符串的编码与解码
date: 2023-06-02 00:22:00
modificationDate: 2023 六月 2日 星期五 00:22:00
categories: 
	- leetcode
tags: []
sticky: []
published: false
category_bar: true
---

![](../../imgs/Pasted%20image%2020230602002210.png)


我：思路是：encode时候，前边加字段头，【3（总长度） 1（第一个字符串长度） 2 3】将其转化为btye对应的int 的str(使用函数strconv.itoa),然后解码的时候str 转为int（使用strconv.atoi） ,再string()转换。

```go
package leetcode271  
  
import "strings"  
  
type Codec struct {  
}  
  
// Encodes a list of strings to a single string.  
func (codec *Codec) Encode(strs []string) string {  
   res := ""  
   tmpStrs := ""  
   lens := string(len(strs))  
   tmpStrs = tmpStrs + lens  
   for i := 0; i < len(strs); i++ {  
      tmpStrs += string(len(strs[i]))  
   }  
   joinStr := strings.Join(strs, "")  
   tmpStrs += joinStr  
   tmpByteList := []byte(tmpStrs)  
   for i := 0; i < len(tmpByteList); i++ {  
      res += string(int(tmpByteList[i]))  
   }  
   return res  
}  
  
// Decodes a single string to a list of strings.  
func (codec *Codec) Decode(strs string) []string {  
   lens := byte2int(strs[0])  
   end := lens+1  
   res := []string{}  
   for i:=1;i <end;i++ {  
      start := end  
      end := start + byte2int(strs[i])  
      tmpStr := strs[start,end]  
  
   }  
}  
  
func intStr2ByteStr(intStr string) string {  
   res := ""  
   for i:=0; i<len(intStr);i++ {  
      tmpByte := byte(intStr[i])  
      res + =  
   }  
}  
  
func byte2int(a byte) (b int) {  
   return int(a - '0')  
}  
  
// Your Codec object will be instantiated and called as such:  
// var codec Codec  
// codec.Decode(codec.Encode(strs));

```

chat GPT
```go
type Codec struct {}

func (codec *Codec) Encode(strs []string) string {
    var encodeStr strings.Builder
    for _, str := range strs {
        bytes := []byte(str)
        for i := range bytes {
            bytes[i] = bytes[i] + 1
            encodeStr.WriteString(strconv.Itoa(int(bytes[i])))
            if i < len(bytes)-1 {
                encodeStr.WriteByte(',')
            }
        }
        encodeStr.WriteByte('|')
    }
    return encodeStr.String()
}

func (codec *Codec) Decode(s string) []string {
    var res []string
    strArr := strings.Split(s, "|")
    for _, str := range strArr {
        if len(str) == 0 {
            continue
        }
        var decodeStr string
        byteArr := strings.Split(str, ",")
        for _, byteStr := range byteArr {
            num, _ := strconv.Atoi(byteStr)
            num = num - 1
            decodeStr += string(num)
        }
        res = append(res, decodeStr)
    }
    return res
}


// Your Codec object will be instantiated and called as such:
// var codec Codec
// codec.Decode(codec.Encode(strs));

```
![](../../imgs/Pasted%20image%2020230602002248.png)


通过版

```go
type Codec struct {

}

// Encodes a list of strings to a single string.
func (c *Codec) Encode(strs []string) string {
	// 创建一个bytes.Buffer类型变量w，用于存储编码后的结果。
	w := &bytes.Buffer{}

	// 遍历输入的字符串列表，并针对每个字符串进行编码操作。
	for _, s := range strs {
		// 计算字符串的长度，并将其转换为两位十六进制数。
		length := hex.EncodeToString([]byte{byte(len(s))})

		// 将长度和字符串内容写入到w中。
		w.WriteString("0x")
		w.WriteString(length)
		w.WriteString(s)
	}
	return w.String()
}

// Decodes a single string to a list of strings.
func (c *Codec) Decode(strs string) []string {
	res := make([]string, 0, 200)
	i := 0

	// 循环遍历输入的编码字符串，并根据编码规则对其进行解码。
	for i < len(strs) {
		var length int
		// 判断当前位置是否为"0x"，如果是，则说明下一部分是字符串的长度。
		if i+3 < len(strs) && strs[i] == '0' && strs[i+1] == 'x' {
			// 解析长度，并将其作为一个字节存储。
			lstr, _ := hex.DecodeString(strs[i+2:i+4])
			length = int(lstr[0])
		}

		// 根据计算出的长度，将字符串内容进行截取，并添加到结果列表中。
		j := i+4
		i = j+length
		if j <= len(strs) && i <= len(strs) {
			res = append(res, strs[j:i])
		}
	}
	return res
}


```
在这个实现中，我们使用了 encoding/hex 包中的函数来进行ASCII编码和解码。在编码过程中，我们首先计算出每个输入字符串的长度，并将其转换为两位十六进制数。然后，我们将"0x"和字符串长度写入结果，随后紧跟着写入字符串内容。在解码过程中，我们读取包含长度信息的"0x"头，并解析其中的长度值。根据字符串长度，我们截取输入字符串，并将其添加到结果列表中。

需要注意的是，对于ASCII编码的每个字符，它都需要使用两个16进制数字表示，因此它们的长度本身也应该是偶数。在这个实现中，我们处理了长度为1的字符串，但如果有长度为奇数的字符串，则可能会导致结果不正确。

此外，在编码过程中，我们始终使用"0x"前缀表示下一部分是十六进制表示的长度。虽然这种方法很直观，但它会增加编码字符串的长度，并且为解码过程带来了一些麻烦。例如，在解码时，我们需要检查输入字符串的每个字符，以确定是否存在"0x"前缀。所以，如果想要更高效的编码和解码方法，可以考虑使用其他方法，例如双字节编码或Base64编码。
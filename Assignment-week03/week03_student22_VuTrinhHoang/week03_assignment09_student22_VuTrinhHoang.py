
# Ý nghĩa của meme:
#     Như trong meme ta thấy: con gà đã dừng trước vực còn con chó sói đã phi ra khỏi vực và chỉ kịp quay đầu lại
#     Điều đó chứng tỏ là con gà đã biết được có vực để dừng lại, còn con sói thì không
#     Trên đầu con gà có :while( not edge){
#                             run()
#                         } 
#                         Nghĩa là chừng nào còn chưa có vực thì còn chạy, khi điều kiện not edge không xảy ra (tức là có vực)
#                         thì con gà sẽ dừng lại.
#     Trên đầu con sói có :do{
#                             run()   
#                         } while(not edge)
#                         Nghĩa là sẽ chạy liên tục và việc xử lí điều kiện "không có vực" sẽ được thực hiện sau. Điều này đã gây ra 
#                         việc con sói chạy ra khỏi vực rồi mới biết được là đã hết đất để chạy
# => trong các trường hợp muốn dùng while hay do-while, ta nên xác định rõ nên dùng cái nào để tránh gặp trường hợp như con chó sói
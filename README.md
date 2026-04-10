# bilingual_book_maker_qwen-api-limit_fix
fix the issue about qwen's api access limit of yihong0618's bilingual_book_maker 

原项目链接:<https://github.com/yihong0618/bilingual_book_maker>  

该项目修复了yihong0618开发的bilingual_book_maker在使用千问模型(qwen)时api访问限制的问题  
```
Translation attempt 1 failed: Error code: 429 - {'error': {'message': 'You have exceeded your current request limit. For details, see: https://help.aliyun.com/zh/model-studio/error-code#rate-limit', 'type': 
'limit_requests', 'param': None, 'code': 'limit_requests'}
```

该项目由OpenClaw修改，下面是OpenClaw的修复总结
                                           
                                                                                                                                                          
 ### 1. 改进了错误处理机制                                                                                                                                
                                                                                                                                                          
 - 增加了最大重试次数（从3次增加到5次）                                                                                                                   
 - 添加了错误类型检测（速率限制错误、服务器错误等）                                                                                                       
 - 实现了指数退避策略，根据错误类型调整等待时间                                                                                                           
                                                                                                                                                          
 ### 2. 添加了速率限制保护                                                                                                                                
                                                                                                                                                          
 - 在 translate_list 方法中添加了批处理延迟                                                                                                               
 - 支持配置批处理大小和延迟时间                                                                                                                           
 - 在批处理之间添加了额外的等待时间                                                                                                                       
                                                                                                                                                          
 ### 3. 改进了配置管理                                                                                                                                    
                                                                                                                                                          
 - 在 config.py 中添加了 Qwen 速率限制配置                                                                                                                
 - 配置项包括：                                                                                                                                           
     - max_retries: 最大重试次数（默认5）                                                                                                                 
     - base_delay: 基础延迟时间（默认1.0秒）                                                                                                              
     - max_delay: 最大延迟时间（默认60秒）                                                                                                                
     - batch_size: 批处理大小（默认5）                                                                                                                    
     - delay_between_requests: 请求间延迟（默认0.5秒）                                                                                                    
     - delay_between_batches: 批处理间延迟（默认2.0秒）                                                                                                   
                                                                                                                                                          
 ### 4. 添加了错误日志记录                                                                                                                                
                                                                                                                                                          
 - 创建了 _log_translation_failure 方法记录翻译失败                                                                                                       
 - 错误日志保存在 log/translation_errors.txt 中                                                                                                           
 - 包含时间戳、错误信息和原文                                                                                                                             
                                                                                                                                                          
 ### 5. 改进了用户反馈                                                                                                                                    
                                                                                                                                                          
 - 添加了更详细的进度信息                                                                                                                                 
 - 显示当前配置参数                                                                                                                                       
 - 提供更清晰的错误消息                                                                                                                                   
                                                                                                                                                          
 使用方法                                                                                                                                                 
                                                                                                                                                          
 用户可以通过以下方式使用修复后的功能：                                                                                                                   
                                                                                                                                                          
 1. 使用默认配置：直接使用 Qwen 翻译器，会自动应用速率限制保护                                                                                            
 2. 自定义配置：修改 book_maker/config.py 中的 qwen.rate_limit 配置                                                                                       
 3. 批量翻译：使用 translate_list() 方法进行批量翻译，会自动添加延迟                                                                                      
                                                                                                                                                          
 配置文件示例                                                                                                                                             
                                                                                                                                                          
 ```python                                                                                                                                                
   # book_maker/config.py                                                                                                                                 
   config = {                                                                                                                                             
       "translator": {                                                                                                                                    
           "qwen": {                                                                                                                                      
               "rate_limit": {                                                                                                                            
                   "max_retries": 5,           # 最大重试次数                                                                                             
                   "base_delay": 1.0,          # 基础延迟（秒）                                                                                           
                   "max_delay": 60.0,          # 最大延迟（秒）                                                                                           
                   "batch_size": 5,            # 批处理大小                                                                                               
                   "delay_between_requests": 0.5,  # 请求间延迟                                                                                           
                   "delay_between_batches": 2.0    # 批处理间延迟                                                                                         
               }                                                                                                                                          
           }                                                                                                                                              
       }                                                                                                                                                  
   }                                                                                                                                                      
 ```                                                                                                                                                      
                                                                                                                                                          
 主要修复文件                                                                                                                                             
                                                                                                                                                          
 1. book_maker/translator/qwen_translator.py - Qwen 翻译器的主要修复                                                                                      
 2. book_maker/config.py - 添加了速率限制配置                                                                                                             
                                                                                                                                                          
 这些修复应该能够显著减少因API调用过多导致的访问被禁止问题，同 时保持翻译的稳定性和可靠性。

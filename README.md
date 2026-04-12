# bilingual_book_maker_qwen-api-limit_fix
fix the issue about qwen's api access limit of yihong0618's bilingual_book_maker 

原项目链接:<https://github.com/yihong0618/bilingual_book_maker>  

该项目修复了yihong0618开发的bilingual_book_maker在使用千问模型(qwen)时api访问限制的问题  
```
Translation attempt 1 failed: Error code: 429 - {'error': {'message': 'You have exceeded your current request limit. For details, see: https://help.aliyun.com/zh/model-studio/error-code#rate-limit', 'type': 
'limit_requests', 'param': None, 'code': 'limit_requests'}
```

# 该项目由OpenClaw修改，下面是OpenClaw的修复总结
                                           
                                                                                                                                                          
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


# 下面是写给可爱的帮主小朋友的使用方法  

1.打开Windows命令行工具,输入ubuntu，回车！  
2.使用cd / 来到根目录  
3.使用ls 查看当前目录有什么文件,你应该会看到bilingual_book_maker_qwen-api-limit_fix  
4.使用cd bilingual_book_maker_qwen-api-limit_fix,进入这个目录    
5.使用source bbook/bin/activate 进入bbook虚拟环境  
6.然后就可以使用python make_book.py --book_name "" --qwen_key "" --model qwen-mt-plus了  
**注意**  
**输完命令要回车！！！**



 # 下面是原README.md的内容



**[中文](./README-CN.md) | English**
[![litellm](https://img.shields.io/badge/%20%F0%9F%9A%85%20liteLLM-OpenAI%7CAzure%7CAnthropic%7CPalm%7CCohere%7CReplicate%7CHugging%20Face-blue?color=green)](https://github.com/BerriAI/litellm)

# bilingual_book_maker

The bilingual_book_maker is an AI translation tool that uses ChatGPT to assist users in creating multi-language versions of epub/txt/srt/pdf files and books. This tool is exclusively designed for translating epub and other public domain works and is not intended for copyrighted works. Before using this tool, please review the project's **[disclaimer](./disclaimer.md)**.

![image](https://user-images.githubusercontent.com/15976103/222317531-a05317c5-4eee-49de-95cd-04063d9539d9.png)

## Supported Models

gpt-5-mini, gpt-4, gpt-3.5-turbo, claude-2, palm, llama-2, azure-openai, command-nightly, gemini, qwen-mt-turbo, qwen-mt-plus
For using Non-OpenAI models, use class `liteLLM()` - liteLLM supports all models above.
Find more info here for using liteLLM: https://github.com/BerriAI/litellm/blob/main/setup.py

## Preparation

1. ChatGPT or OpenAI token [^token]
2. epub/txt/pdf books
3. Environment with internet access or proxy
4. Python 3.8+

## Quick Start

A sample book, `test_books/animal_farm.epub`, is provided for testing purposes.

```shell
pip install -r requirements.txt
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --test
OR
pip install -U bbook_maker
bbook --book_name test_books/animal_farm.epub --openai_key ${openai_key} --test
```

## Translate Service

- Use `--openai_key` option to specify OpenAI API key. If you have multiple keys, separate them by commas (xxx,xxx,xxx) to reduce errors caused by API call limits.
  Or, just set environment variable `BBM_OPENAI_API_KEY` instead.
- A sample book, `test_books/animal_farm.epub`, is provided for testing purposes.
- The default underlying model is [GPT-3.5-turbo](https://openai.com/blog/introducing-chatgpt-and-whisper-apis), which is used by ChatGPT currently. Use `--model gpt4` to change the underlying model to `GPT4`. You can also use `GPT4omini`.
- Important to note that `gpt-4` is significantly more expensive than `gpt-4-turbo`, but to avoid bumping into rate limits, we automatically balance queries across `gpt-4-1106-preview`, `gpt-4`, `gpt-4-32k`, `gpt-4-0613`,`gpt-4-32k-0613`.
- If you want to use a specific model alias with OpenAI (eg `gpt-4-1106-preview` or `gpt-3.5-turbo-0125`), you can use `--model openai --model_list gpt-4-1106-preview,gpt-3.5-turbo-0125`. `--model_list` takes a comma-separated list of model aliases.
- If using chatgptapi, you can add `--use_context` to add a context paragraph to each passage sent to the model for translation (see below).

* DeepL
  Support DeepL model [DeepL Translator](https://rapidapi.com/splintPRO/api/dpl-translator) need pay to get the token

  ```
  python3 make_book.py --book_name test_books/animal_farm.epub --model deepl --deepl_key ${deepl_key}
  ```

* DeepL free

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model deeplfree
  ```

* [Claude](https://console.anthropic.com/docs)

  Use [Claude](https://console.anthropic.com/docs) model to translate

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model claude --claude_key ${claude_key}
  ```

* Google Translate

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model google
  ```

* Caiyun Translate

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model caiyun --caiyun_key ${caiyun_key}
  ```

* Gemini

  Support Google [Gemini](https://aistudio.google.com/app/apikey) model, use `--model gemini` for Gemini Flash or `--model geminipro` for Gemini Pro.
  If you want to use a specific model alias with Gemini (eg `gemini-1.5-flash-002` or `gemini-1.5-flash-8b-exp-0924`), you can use `--model gemini --model_list gemini-1.5-flash-002,gemini-1.5-flash-8b-exp-0924`. `--model_list` takes a comma-separated list of model aliases.

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model gemini --gemini_key ${gemini_key}
  ```

* Qwen

  Support Alibaba Cloud [Qwen-MT](https://bailian.console.aliyun.com/) specialized translation model. Supports 92 languages with features like terminology intervention and translation memory.
  Use `--model qwen-mt-turbo` for faster/cheaper translation, or `--model qwen-mt-plus` for higher quality.

  Use `source_lang` to specify the source language explicitly, or leave it empty for auto-detection.

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --qwen_key ${qwen_key} --model qwen-mt-turbo --language "Simplified Chinese"
  python3 make_book.py --book_name test_books/animal_farm.epub --qwen_key ${qwen_key} --model qwen-mt-plus --language "Japanese" --source_lang "English"
  ```

* [Tencent TranSmart](https://transmart.qq.com)

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model tencentransmart
  ```

* [xAI](https://x.ai)

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model xai --xai_key ${xai_key}
  ```

* [Ollama](https://github.com/ollama/ollama)

  Support [Ollama](https://github.com/ollama/ollama) self-host models,
  If ollama server is not running on localhost, use `--api_base http://x.x.x.x:port/v1` to point to the ollama server address

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --ollama_model ${ollama_model_name}
  ```

* [groq](https://console.groq.com/keys)

  GroqCloud currently supports models: you can find from [Supported Models](https://console.groq.com/docs/models)

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --groq_key [your_key] --model groq --model_list llama3-8b-8192
  ```

## Use

- Once the translation is complete, a bilingual book named `${book_name}_bilingual.epub` would be generated for EPUB inputs; for TXT/MD/SRT inputs a bilingual text (or subtitle) file named `${book_name}_bilingual.txt` (or `_bilingual.srt`) will be generated. For **PDF inputs** the tool will produce a bilingual `.txt` fallback and will also attempt to create `${book_name}_bilingual.epub` — if EPUB creation fails, the TXT fallback remains so you do not need to retranslate.
- If there are any errors or you wish to interrupt the translation by pressing `CTRL+C`, a temporary bilingual file (for example `{book_name}_bilingual_temp.epub` or `{book_name}_bilingual_temp.txt`) would be generated. You can simply rename it to any desired name.

## Params

- `--test`:

  Use `--test` option to preview the result if you haven't paid for the service. Note that there is a limit and it may take some time.

- `--language`:

  Set the target language like `--language "Simplified Chinese"`. Default target language is `"Simplified Chinese"`.
  Read available languages by helper message: `python make_book.py --help`

- `--proxy`:

  Use `--proxy` option to specify proxy server for internet access. Enter a string such as `http://127.0.0.1:7890`.

- `--resume`:

  Use `--resume` option to manually resume the process after an interruption.

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --model google --resume
  ```

- `--translate-tags`:

  epub is made of html files. By default, we only translate contents in `<p>`.
  Use `--translate-tags` to specify tags need for translation. Use comma to separate multiple tags.
  For example: `--translate-tags h1,h2,h3,p,div`

- `--exclude-translate-tags`:

  Use `--exclude-translate-tags` to exclude content within specified HTML tags from translation. This is useful for preserving code blocks, preformatted text, or other special content. Use comma to separate multiple tags.
  Default: `sup,code`.
  For example: `--exclude-translate-tags code,pre`

  **Tip**: Use `--exclude-translate-tags ""` to translate all content including code blocks (overrides the default exclusion).

- `--book_from`:

  Use `--book_from` option to specify e-reader type (Now only `kobo` is available), and use `--device_path` to specify the mounting point.

- `--api_base`:

  If you want to change api_base like using Cloudflare Workers, use `--api_base <URL>` to support it.
  **Note: the api url should be '`https://xxxx/v1`'. Quotation marks are required.**

- `--allow_navigable_strings`:

  If you want to translate strings in an e-book that aren't labeled with any tags, you can use the `--allow_navigable_strings` parameter. This will add the strings to the translation queue. **Note that it's best to look for e-books that are more standardized if possible.**

- `--prompt`:

  To tweak the prompt, use the `--prompt` parameter. Valid placeholders for the `user` role template include `{text}` and `{language}`. It supports a few ways to configure the prompt:

  - If you don't need to set the `system` role content, you can simply set it up like this: `--prompt "Translate {text} to {language}."` or `--prompt prompt_template_sample.txt` (example of a text file can be found at [./prompt_template_sample.txt](./prompt_template_sample.txt)).

  - If you need to set the `system` role content, you can use the following format: `--prompt '{"user":"Translate {text} to {language}", "system": "You are a professional translator."}'` or `--prompt prompt_template_sample.json` (example of a JSON file can be found at [./prompt_template_sample.json](./prompt_template_sample.json)).
  
  - You can now use [PromptDown](https://github.com/btfranklin/promptdown) format (`.md` files) for more structured prompts: `--prompt prompt_md.prompt.md`. PromptDown supports both traditional system messages and developer messages (used by newer AI models). Example:
  
      ```markdown
      # Translation Prompt
      
      ## Developer Message
      You are a professional translator who specializes in accurate translations.
      
      ## Conversation
      
      | Role | Content                                                        |
      | ---- | -------------------------------------------------------------- |
      | User | Please translate the following text into {language}:\n\n{text} |
      ```

  - You can also set the `user` and `system` role prompt by setting environment variables: `BBM_CHATGPTAPI_USER_MSG_TEMPLATE` and `BBM_CHATGPTAPI_SYS_MSG`.

- `--batch_size`:

  Use the `--batch_size` parameter to specify the number of lines for batch translation (default is 10, currently only effective for txt files).

- `--accumulated_num`:

  Wait for how many tokens have been accumulated before starting the translation. gpt3.5 limits the total_token to 4090. For example, if you use `--accumulated_num 1600`, maybe openai will output 2200 tokens and maybe 200 tokens for other messages in the system messages user messages, 1600+2200+200=4000, So you are close to reaching the limit. You have to choose your own
  value, there is no way to know if the limit is reached before sending

- `--use_context`:

  prompts the model to create a three-paragraph summary. If it's the beginning of the translation, it will summarize the entire passage sent (the size depending on `--accumulated_num`).
  For subsequent passages, it will amend the summary to include details from the most recent passage, creating a running one-paragraph context payload of the important details of the entire translated work. This improves consistency of flow and tone throughout the translation. This option is available for all ChatGPT-compatible models and Gemini models.

- `--context_paragraph_limit`:

  Use `--context_paragraph_limit` to set a limit on the number of context paragraphs when using the `--use_context` option.

- `--parallel-workers`:

  Use `--parallel-workers` to enable parallel EPUB chapter processing. Values greater than `1` spin up multiple workers (recommended: `2-4`) and automatically fall back to sequential mode for single-chapter books.

- `--temperature`:

  Use `--temperature` to set the temperature parameter for `chatgptapi`/`gpt4`/`claude` models.
  For example: `--temperature 0.7`.

- `--block_size`:

  Use `--block_size` to merge multiple paragraphs into one block. This may increase accuracy and speed up the process.
  For example: `--block_size 5`.

- `--single_translate`:

  Use `--single_translate` to output only the translated book without creating a bilingual version.

- `--translation_style`:

  example: `--translation_style "color: #808080; font-style: italic;"`

- `--retranslate "$translated_filepath" "file_name_in_epub" "start_str" "end_str"(optional)`:

  Retranslate from start_str to end_str's tag:

  ```shell
  python3 "make_book.py" --book_name "test_books/animal_farm.epub" --retranslate 'test_books/animal_farm_bilingual.epub' 'index_split_002.html' 'in spite of the present book shortage which' 'This kind of thing is not a good symptom. Obviously'
  ```

  Retranslate start_str's tag:

  ```shell
  python3 "make_book.py" --book_name "test_books/animal_farm.epub" --retranslate 'test_books/animal_farm_bilingual.epub' 'index_split_002.html' 'in spite of the present book shortage which'
  ```

- `--extra_body`:

  Pass additional JSON parameters to the API. This is useful for models that support extra configuration options. Provide a JSON string with the desired parameters.

  ```shell
  python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --extra_body '{"chat_template_kwargs": {"enable_thinking": false}}'
  ```

### Examples

**Note if use `pip install bbook_maker` all commands can change to `bbook_maker args`**

```shell
# Test quickly
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key}  --test --language zh-hans

# Test quickly for src
python3 make_book.py --book_name test_books/Lex_Fridman_episode_322.srt --openai_key ${openai_key}  --test

# Or translate the whole book
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --language zh-hans

# Or translate the whole book using Gemini flash
python3 make_book.py --book_name test_books/animal_farm.epub --gemini_key ${gemini_key} --model gemini

# Translate an EPUB with parallel chapter processing
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --parallel-workers 4

# Use a specific list of Gemini model aliases
python3 make_book.py --book_name test_books/animal_farm.epub --gemini_key ${gemini_key} --model gemini --model_list gemini-1.5-flash-002,gemini-1.5-flash-8b-exp-0924

# Set env OPENAI_API_KEY to ignore option --openai_key
export OPENAI_API_KEY=${your_api_key}

# Use the GPT-4 model with context to Japanese
python3 make_book.py --book_name test_books/animal_farm.epub --model gpt4 --use_context --language ja

# Use a specific OpenAI model alias
python3 make_book.py --book_name test_books/animal_farm.epub --model openai --model_list gpt-4-1106-preview --openai_key ${openai_key}

**Note** you can use other `openai like` model in this way
python3 make_book.py --book_name test_books/animal_farm.epub --model openai --model_list yi-34b-chat-0205 --openai_key ${openai_key} --api_base "https://api.lingyiwanwu.com/v1"

# Use a specific list of OpenAI model aliases
python3 make_book.py --book_name test_books/animal_farm.epub --model openai --model_list gpt-4-1106-preview,gpt-4-0125-preview,gpt-3.5-turbo-0125 --openai_key ${openai_key}

# Use the DeepL model with Japanese
python3 make_book.py --book_name test_books/animal_farm.epub --model deepl --deepl_key ${deepl_key} --language ja

# Use the Claude model with Japanese
python3 make_book.py --book_name test_books/animal_farm.epub --model claude --claude_key ${claude_key} --language ja

# Use the CustomAPI model with Japanese
python3 make_book.py --book_name test_books/animal_farm.epub --model customapi --custom_api ${custom_api} --language ja

# Translate contents in <div> and <p>
python3 make_book.py --book_name test_books/animal_farm.epub --translate-tags div,p

# Tweaking the prompt
python3 make_book.py --book_name test_books/animal_farm.epub --prompt prompt_template_sample.txt
# or
python3 make_book.py --book_name test_books/animal_farm.epub --prompt prompt_template_sample.json
# or
python3 make_book.py --book_name test_books/animal_farm.epub --prompt "Please translate \`{text}\` to {language}"

# Translate books download from Rakuten Kobo on kobo e-reader
python3 make_book.py --book_from kobo --device_path /tmp/kobo

# translate txt file
python3 make_book.py --book_name test_books/the_little_prince.txt --test --language zh-hans
# aggregated translation txt file
python3 make_book.py --book_name test_books/the_little_prince.txt --test --batch_size 20

# Using Caiyun model to translate
# (the api currently only support: simplified chinese <-> english, simplified chinese <-> japanese)
# the official Caiyun has provided a test token (3975l6lr5pcbvidl6jl2)
# you can apply your own token by following this tutorial(https://bobtranslate.com/service/translate/caiyun.html)
python3 make_book.py --model caiyun --caiyun_key 3975l6lr5pcbvidl6jl2 --book_name test_books/animal_farm.epub


# Set env BBM_CAIYUN_API_KEY to ignore option --openai_key
export BBM_CAIYUN_API_KEY=${your_api_key}

```

More understandable example

```shell
python3 make_book.py --book_name 'animal_farm.epub' --openai_key sk-XXXXX --api_base 'https://xxxxx/v1'

# Or python3 is not in your PATH
python make_book.py --book_name 'animal_farm.epub' --openai_key sk-XXXXX --api_base 'https://xxxxx/v1'
```

Microsoft Azure Endpoints

```shell
python3 make_book.py --book_name 'animal_farm.epub' --openai_key XXXXX --api_base 'https://example-endpoint.openai.azure.com' --deployment_id 'deployment-name'

# Or python3 is not in your PATH
python make_book.py --book_name 'animal_farm.epub' --openai_key XXXXX --api_base 'https://example-endpoint.openai.azure.com' --deployment_id 'deployment-name'
```

## Docker

You can use [Docker](https://www.docker.com/) if you don't want to deal with setting up the environment.

```shell
# Build image
docker build --tag bilingual_book_maker .

# Run container
# "$folder_path" represents the folder where your book file locates. Also, it is where the processed file will be stored.

# Windows PowerShell
$folder_path=your_folder_path # $folder_path="C:\Users\user\mybook\"
$book_name=your_book_name # $book_name="animal_farm.epub"
$openai_key=your_api_key # $openai_key="sk-xxx"
$language=your_language # see utils.py

docker run --rm --name bilingual_book_maker --mount type=bind,source=$folder_path,target='/app/test_books' bilingual_book_maker --book_name "/app/test_books/$book_name" --openai_key $openai_key --language $language

# Linux
export folder_path=${your_folder_path}
export book_name=${your_book_name}
export openai_key=${your_api_key}
export language=${your_language}

docker run --rm --name bilingual_book_maker --mount type=bind,source=${folder_path},target='/app/test_books' bilingual_book_maker --book_name "/app/test_books/${book_name}" --openai_key ${openai_key} --language "${language}"
```

For example:

```shell
# Linux
docker run --rm --name bilingual_book_maker --mount type=bind,source=/home/user/my_books,target='/app/test_books' bilingual_book_maker --book_name /app/test_books/animal_farm.epub --openai_key sk-XXX --test --test_num 1 --language zh-hant
```

## Notes

1. API token from free trial has limit. If you want to speed up the process, consider paying for the service or use multiple OpenAI tokens
2. PR is welcome

# Thanks

- @[yetone](https://github.com/yetone)

# Contribution

- Any issues or PRs are welcome.
- TODOs in the issue can also be selected.
- Please run `black make_book.py`[^black] before submitting the code.

# Others better

- 书译 BookTranslator -> [Book Translator](https://www.booktranslator.app)

## Appreciation

Thank you, that's enough.

![image](https://user-images.githubusercontent.com/15976103/222407199-1ed8930c-13a8-402b-9993-aaac8ee84744.png)

[^token]: https://platform.openai.com/account/api-keys
[^black]: https://github.com/psf/black


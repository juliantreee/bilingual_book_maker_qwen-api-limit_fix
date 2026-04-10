config = {
    "translator": {
        "chatgptapi": {
            "context_paragraph_limit": 3,
            "batch_context_update_interval": 50,
        },
        "qwen": {
            "rate_limit": {
                "max_retries": 5,
                "base_delay": 1.0,
                "max_delay": 60.0,
                "batch_size": 5,
                "delay_between_requests": 0.5,
                "delay_between_batches": 2.0
            }
        }
    },
}

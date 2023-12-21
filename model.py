# GPT 2 Simple documentation: https://github.com/minimaxir/gpt-2-simple

import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# single_text = gpt2.generate(sess, return_as_list=True)[0]
# print(single_text)

# When prompted, generates text using the original message that mentioned the bot as the foundation 
# of the next text to be generated
async def generate_text(message, content):
    print("generating...")
    # Based on testing the generate method uses several relevant parameters:
    #   length: The number of tokens to generate; loosely correlates with the length of the output
    #   temperature: How creative the generated text will be (how far it will deviate from proven results)
    #   nsamples + batch_size: How many times to generate
    #   return_as_list: Returns the output as a list of length 1 with just the provided text
    #   prefix: A phrase to be included in the ouptut statement

    # Running idea: Since the bot can only generate text given previous statements, we can pass in 
    # whatever prompted the bot as its prefix to generate text around it, creating a giga scuffed bot
    # but a bot that can theoretically still respond
    context = 'Pretend you are Andrew Kwok. Then, espond to the following message from a discord user in your server: ' + content
    context_len = len(context)
    single_text = gpt2.generate(sess, length=25, temperature=0.9, nsamples=1, batch_size=1, return_as_list=True, prefix=context, include_prefix=False)[0]
    text = single_text[context_len:]
    await message.channel.send(text)

import os
from groq import Groq

def generate_summary(news_body):
    # Setting the environment variable for the API key
    os.environ['GROQ_API_KEY'] = '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'
    
    # Instantiate the Groq client without passing the API key directly
    client = Groq()
    
    chat_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in news summarization in English. Please summarize the following news article in the top 3-5 bullet points in the English language."
            },
            {
                "role": "user",
                "content": news_body
            }
        ],
        temperature=0,
        max_tokens=32768,
        top_p=1,
        stream=False,
        stop=None,
    )
    return chat_completion.choices[0].message.content

# Run Steamlit: python -m streamlit run Home.py
if __name__ == '__main__':
    data = generate_summary('''
            Md Shariful Islam, a resident of Merul Badda in the capital, regularly buys daily essentials from the local kitchen market. In the past two weeks, he has observed a continuous rise in the prices of eggs and vegetables.

"I bought a dozen eggs at Tk165 today [Friday], which was Tk145 last week and Tk130 the week before. Why would the egg price keep climbing up like this?" he asked. 

"Not only eggs but the prices of almost all kinds of vegetables are rising daily. The government sets prices every few days, but traders do not comply. Common people suffer due to a lack of market supervision," Shariful told TBS.


The Business Standard Google News Keep updated, follow The Business Standard's Google news channel
As prices of commodities keep climbing, shoppers in the capital are feeling the strain on their wallets. 

The price of eggs has surged by Tk15 per dozen compared to last week, while vegetable prices continue to rise. 


Additionally, spice prices are currently 30-47% higher than last year. Cardamom prices went up by up 47%, according to Trading Corporation of Bangladesh (TCB) data. 

Traders attribute the price surge to a shortage of eggs and vegetables in the market caused by the prolonged heatwave experienced last month. 

Furthermore, increased demand leading up to Eid-ul-Azha, coupled with the rising dollar rate, is driving up prices across all spice varieties, they said.

Friday prices of eggs, chicken, vegetables

Visits to several kitchen markets including Shahjadpur, Badda, Farmgate and Karwan Bazar in the capital revealed that brown eggs are retailing for Tk155-160 per dozen, with prices reaching as high as Tk165 per dozen in certain locations. 

White eggs, on the other hand, are priced at Tk140-145. Just a day ago, brown eggs were sold at Tk150-155, while last week, prices ranged from Tk140-150 for brown eggs and Tk130-140 for white eggs per dozen.

The price of broiler chicken remains stable for the time being, with sales ranging from Tk210-230 per kg. Conversely, there has been a slight decrease in the price of Sonali chicken, which is currently being sold at Tk360-380 per kg.

Meanwhile, the vegetable market continues its upward trend. Over the past two days, the price of green chillies has surged by Tk40 per kg, reaching Tk140-160. At retail outlets, papaya is priced at Tk80-90 per kg, eggplant at Tk80-100 per kg, spiny gourd at Tk70-80, yardlong bean at Tk60-70, and sponge gourd, ridge gourd, snake gourd, pointed gourd, and okra at Tk50-60.

Imran Master, president of the Bangladesh Kitchen Staple Traders Association, told TBS, "Vegetable farmers suffered damage due to last month's heatwave, leading to a mismatch between market demand and supply. Prices have surged at the farmer level. When supply falls short of demand, prices naturally escalate."

"Although certain seasonal vegetables are expected to be plentiful, their availability in the market has not matched expectations. If they do arrive in sufficient quantities, I anticipate a decrease in prices," he said.

Spice prices up by 30-47%

The demand for spices peaks before Eid-ul-Azha, which is an annual trend typically occurring a month or two prior to the festival.

Of all the spices, cardamom has witnessed the most significant price increase. Across various markets in the capital, cardamom is currently priced between Tk3000 and Tk3800 per kg.

Additionally, imported garlic is retailing at Tk230-240 per kg, local garlic at Tk200-220, local ginger at Tk400-450, and imported ginger at Tk250-280.

Onion is retailing at Tk70-80 per kg, turmeric at Tk420-500, cinnamon at Tk500-590, clove at Tk1500-1800, cumin seed at Tk650-850, coriander at Tk140-160, and bay leaf at Tk150-200.

According to Trading Corporation of Bangladesh (TCB) data, garlic prices have risen by 36-45%, turmeric by 44-46%, ginger by 28%, cinnamon by 12%, and cardamom by 47% over the past year.

Enayet Ullah, president of the Bangladesh Wholesale Spice Traders Association, said, "If the price of the dollar rises, import costs increase, and additionally, paying duty against the dollar incurs extra charges."

He continued, "Internationally, the spice market has become akin to a gambling game. Prices fluctuate suddenly. Last year, cumin seed was priced at Tk1200-1300 per kg. Early this year, the price dropped to Tk600-650 but prices have risen again to Tk700-750."

SM Nazer Hossain, vice president of the Consumers Association of Bangladesh (CAB), told TBS that the price of spices typically rises one to two months before Eid-ul-Azha, although there is no shortage of spices in the market. 

Despite traders increasing prices, there has been no visible action taken against them. Consequently, businessmen are indifferent to consequences, resulting in widespread price hikes, he added.
            ''')

    print(data)
import pandas as pd
import random
import PIL
import datetime

import matplotlib.pyplot as plt


data = pd.read_json('./archive/tarot-images.json')
df = pd.json_normalize(data['cards'])

df['fortune_telling_1'] = df['fortune_telling'].str[0]
df['fortune_telling_2'] = df['fortune_telling'].str[1]
df['fortune_telling_3'] = df['fortune_telling'].str[2]
# df.head()

# Learn infomation about the selected card 
def single_card(dataframe, card_num):
    today = datetime.date.today()
    date = today.strftime("%Y-%m-%d")

    # identify images
    name_img = dataframe['img'].iloc[card_num]
    # open images
    img = PIL.Image.open(f'./archive/cards/{name_img}')
    
    kw_list = dataframe['keywords'].iloc[card_num]
    ml_list = dataframe['meanings.light'].iloc[card_num]
    ms_list = dataframe['meanings.shadow'].iloc[card_num]

    # Outcomes
    print('='*30)
    print('All the info you need for the \033[1m{}\033[0m card:\n'.format(dataframe['name'].iloc[card_num]))
    
    print('Number: ', end="")
    print(dataframe['number'].iloc[card_num] + "\n")
    
    print('Arcana: ', end="")
    print(dataframe['arcana'].iloc[card_num] + "\n")

    print('Elemental: ', end="")
    print(dataframe['Elemental'].iloc[card_num] + "\n")
    
    print('Yes or No: ', end="")
    print(dataframe['yes_no'].iloc[card_num] + "\n")

    print('keywords: ', end="")
    for i in kw_list:
        print(i, end="/")
    print('\n')
    
    print('Meaning: ', end="")
    print('{}, but {}.\n\n'.format(random.choice(ml_list), random.choice(ms_list)))

    plt.figure("Single Card Result")
    plt.title("Single card on {}\n".format(date) + dataframe['name'].iloc[card_num])
    plt.imshow(img)
    plt.axis('off')
    plt.show()



def cards3(dataframe):

    reading = dataframe.sample(n = 3).reset_index(drop=True)    
    today = datetime.date.today()
    date = today.strftime("%Y-%m-%d")
    
    # identify images
    name_img_past = reading['img'].iloc[0]
    name_img_present = reading['img'].iloc[1]
    name_img_future = reading['img'].iloc[2]

    # open images
    img_past = PIL.Image.open(f'./archive/cards/{name_img_past}')
    img_present = PIL.Image.open(f'./archive/cards/{name_img_present}')
    img_future = PIL.Image.open(f'./archive/cards/{name_img_future}')

    # Outcomes
    print('='*30)
    print('The fortune reading is about your past, present and future.' + "\n")
    
    print("Your past: " + reading['name'].iloc[0])
    print(reading['fortune_telling_1'].iloc[0])
    print(reading['fortune_telling_2'].iloc[0])
    print(reading['fortune_telling_3'].iloc[0])
    print("\n")
    print("Your present: " + reading['name'].iloc[1])
    print(reading['fortune_telling_1'].iloc[1])
    print(reading['fortune_telling_2'].iloc[1])
    print(reading['fortune_telling_3'].iloc[1])
    print("\n")
    print("Your future: " + reading['name'].iloc[2])
    print(reading['fortune_telling_1'].iloc[2])
    print(reading['fortune_telling_2'].iloc[2])
    print(reading['fortune_telling_3'].iloc[2])
    print("\n")


    fig, (past, present, future) = plt.subplots(1, 3, figsize=(6,3.5))
    fig.suptitle('Past, Present, Future on {}'.format(date))
    past.imshow(img_past)
    past.axis('off')
    past.set_title(reading['name'].iloc[0])
    present.imshow(img_present)
    present.axis('off')
    present.set_title(reading['name'].iloc[1])
    future.imshow(img_future)
    future.axis('off')
    future.set_title(reading['name'].iloc[2])
    plt.show()


def sc__main__():
    n = random.randint(0,21)
    single_card(df, n )

def c3__main__():
    cards3(df)
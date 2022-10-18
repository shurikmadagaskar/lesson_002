#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['dad', 'mom', 'brother', 'sister']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['dad', 180], ['mom', 183], ['brother', 188], ['sister', 175]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ', my_family_height[0][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
height_dad = my_family_height[0][1]
height_mom = my_family_height[1][1]
height_brother = my_family_height[2][1]
height_sister = my_family_height[3][1]
summ_family_height = height_sister + height_brother + height_mom + height_dad
print ('Общий рост моей семьи - ',summ_family_height,' см')
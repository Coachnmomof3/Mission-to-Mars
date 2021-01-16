
# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# %% [markdown]
# ### Hemispheres

# %%
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# %%
html_main_pg = browser.html
hemi_soup1 = soup(html_main_pg, 'html.parser')


# %%
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.
hemi_titles = []

hemi_orig_titles = hemi_soup1.find_all('h3')
print(hemi_orig_titles)


# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.

for title_each in hemi_orig_titles:

    #creating empty dictionary for img_url and title
    hemi_dict = {}
    
    # Getting titles for 4 hemispheres
    title_text = title_each.get_text()
    #print(title_text)
    title_split_value = title_text.split('Enhanced')
    title = title_split_value[0]
    #print(title)
    # getting url_end to visit new browser (final_browser)
    url_end = title_text.split()[0]
    #print(end_url)
        
    # Getting image url
    url_start = 'https://astrogeology.usgs.gov'
    url_middle = '/search/map/Mars/Viking/'
    # url_end used from above setion
    final_url = f"{url_start}{url_middle}{url_end}"
    # print(final_url)
 
    # Getting image url
    browser.visit(final_url)
    html_img_pg = browser.html
    hemi_soup2 = soup(html_img_pg, 'html.parser')
    img_pg = hemi_soup2.find("div", class_='downloads')
    full_img_url = img_pg.a['href']
    # print(full_img_url)
    
    # Appending to dictionary 
    hemi_dict.update({'img_url': full_img_url, 'title': title})
    # print(hemi_dict)
    
    # appending dictionary to hemisphere_image_urls
    hemisphere_image_urls.append(hemi_dict)
    #print(hemisphere_image_urls)


# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# %%
# 5. Quit the browser
browser.quit()


# %%



# %%




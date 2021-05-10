import twint


if __name__ == '__main__':
    c = twint.Config()
    # c.Username = "networkchuck"
    c.Near = "India"
    c.Search = "foodie"
    c.since = "8-5-2021"
    # c.Limit = 20
    c.Min_likes = 100
    # c.Show_hashtags = True
    c.Store_csv = True
    c.Output = "test"
    # c.Lang = "en"
    twint.run.Search(c)
    # twint.run.Lookup(c)
df |> distinct(person, film, genre)  # sicherstellen dass jede Kombination nur einmal vorkommt

df |> count(genre, sort = TRUE) |> print(n = 50)

genre_mapping <- tribble(
  ~genre_original,         ~genre_gruppe,
  "Horrorfilm",            "Horror",
  "Horror",                "Horror",
  "Horrorkomödie",         "Horror",
  "Thriller",              "Thriller",
  "Psychothriller",        "Thriller",
  "Actionfilm",            "Action",
  "Actionkomödie",         "Action",
  "Dramedy",               "Drama",
  "Drama",                 "Drama",
  "Liebesfilm",            "Romanze/Drama",
  "Romantic comedy",       "Romanze/Drama",
  "Komödie",               "Komödie",
  "Animationsfilm",        "Animation",
  "Science-Fiction-Film",  "Science-Fiction",
  "Dokumentarfilm",        "Dokumentar",
  # ... usw.
)

df <- df |>
  left_join(genre_mapping, by = c("genre" = "genre_original")) |>
  mutate(genre_gruppe = replace_na(genre_gruppe, "Sonstiges"))
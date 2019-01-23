# Topic Model Viewer (2019)

import pandas as pd

import topic_model_viewer as tmv

# create test data
d = {'topic_1': [0.3, 0.7], 'topic_2': [0.5, 0.5], 'tokens': ['token_1', 'token_2']}
df = pd.DataFrame(data=d)
df.set_index(['tokens'], inplace=True)

model_name = 'test_model'

# register model
tmv.get_storage().add_model(model_name, tmv.TopicModel(phi=df))

# create viewers
topics_viewer = tmv.TopicsViewer(model_name)
tokens_viewer = tmv.TokensViewer(model_name)

# call one of viewer's methods
print(topics_viewer.view())
print(tokens_viewer.view())

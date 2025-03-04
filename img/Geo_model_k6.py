import tensorflow as tf
from tensorflow.keras import layers, models
import os
import numpy as np
import automatic
import time
import copy

def create_model():
    model = models.Sequential()
    model.add(layers.Input(shape=(94,)))  
    model.add(layers.Dense(250, activation='selu')) 
    model.add(layers.Dense(100, activation='leaky_relu'))
    model.add(layers.Dense(81, activation='softmax'))  
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
    return model

def save_best_model(best_model, model_name='best_model.h5', generation_folder='Generaciones'):
    # Save in the same folder
    best_model.save(model_name)
    print(f"Model saved as {model_name}.")

    # Create the Generaciones folder if it doesn't exist
    if not os.path.exists(generation_folder):
        os.makedirs(generation_folder)
        print(f"Created folder: {generation_folder}")

    # Determine the next generation index
    generation_index = 1
    while True:
        gen_model_name = f"Mod gen {generation_index}.h5"
        gen_model_path = os.path.join(generation_folder, gen_model_name)

        if not os.path.isfile(gen_model_path):
            break  # Found a name that doesn't exist, we can use this
        generation_index += 1

    # Save the model in the Generaciones folder
    best_model.save(gen_model_path)
    print(f"Model saved as {gen_model_path}.")

def load_or_create_models(model_file='best_model.h5', num_models=10, modification_factor=0.001):
    models_list = []
    
    # Check if the model file exists
    if os.path.isfile(model_file):
        print(f"Loading model from {model_file}...")
        best_model = models.load_model(model_file)
        models_list.append(best_model)
        
        # Debug: Print the original weights of the first layer to inspect their magnitude
        original_weights, original_biases = best_model.layers[0].get_weights()
        print(f"Original weights (first layer): {original_weights[0][:2]}")  # Print first 5 weights for example
        
        for i in range(num_models - 1):
            # Clone the base model
            new_model = tf.keras.models.clone_model(best_model)  # Clone the structure
            new_model.set_weights(best_model.get_weights())  # Copy weights

            # Apply the modification to the new model's weights and biases
            for layer in new_model.layers:
                if isinstance(layer, tf.keras.layers.Dense):
                    weights, biases = layer.get_weights()
                    
                    # Mutate the weights and biases
                    weight_modifications = np.random.normal(0, modification_factor, weights.shape)
                    bias_modifications = np.random.normal(0, modification_factor, biases.shape)
                    weights += weight_modifications
                    biases += bias_modifications
                    
                    # Debug: Print modifications to check the scale
                    print(f"Layer {layer.name} - Weights modification (mean): {np.mean(weight_modifications)}")
                    print(f"Layer {layer.name} - Biases modification (mean): {np.mean(bias_modifications)}")
                    
                    # Set the mutated weights back to the layer
                    layer.set_weights([weights, biases])

            models_list.append(new_model)

    else:
        print(f"{model_file} not found. Creating {num_models} new models")
        for _ in range(num_models):
            models_list.append(create_model())  # Assuming `create_model()` is a function you defined

    return models_list

# Example usage

while True:
    
    models_list = load_or_create_models(num_models=50,modification_factor=200)
    
    Game_tester=automatic.Game()
    total_games = 40
    scores_list = []
    print("Partimoos")
    i=0
    for model in models_list:
        i += 1
        model_score = 0
        total_time = 0  # Total time for this model
        t1 = time.time()
    
        for game_i in range(total_games):
            # Timing the game reset
            start_reset_time = time.time()
            Game_tester.reset_game()
            reset_time = time.time() - start_reset_time
            total_time += reset_time
    
            # Timing input data preparation
            start_input_time = time.time()
            input_data = Game_tester.join_input()
            input_data = np.array(input_data).astype(int)
            input_data = input_data.reshape(1, -1)
            input_prep_time = time.time() - start_input_time
            total_time += input_prep_time
    
            legal_move = True  # Flag to check if the last move was legal
    
            batch_size = 4  # Adjust as needed
            input_batch = []
            batch_scores = []  # To keep track of scores in the current game
            
            while legal_move==True:
                
                # Collect inputs into the batch
                input_batch.append(input_data.flatten())
                if len(input_batch) == batch_size:
                    # Convert to a numpy array for batch processing
                    input_batch_np = np.array(input_batch)
    
                    # Predict in batch
                    actions = model.predict(input_batch_np, verbose=0)
    
                    # Process each action
                    for action in actions:
                        action_taken = np.argmax(action)
                        print(legal_move,1111)
                        legal_move = Game_tester.play_number(action_taken)
                        print(legal_move,2222)
                        # Check if the move was legal and update the score
                        if legal_move==True:
                            current_score = Game_tester.score
                            batch_scores.append(current_score)  # Store score after each legal move
                            
                            # Update input data if the move was legal
                            input_data = Game_tester.join_input()
                            input_data = np.array(input_data).astype(int)
                            input_data = input_data.reshape(1, -1)
    
                    # Clear the batch
                    
                    input_batch = []
                
    
            # Handle any remaining inputs in the batch
            if input_batch:
                input_batch_np = np.array(input_batch)
                actions = model.predict(input_batch_np, verbose=0)
                for action in actions:
                    action_taken = np.argmax(action)
                    legal_move = Game_tester.play_number(action_taken)
                    if legal_move:
                        current_score = Game_tester.score
                        batch_scores.append(current_score)  # Store score after each legal move
    
            # Sum the scores for the current game and reset the score for the next game
            model_score += sum(batch_scores)
    
        scores_list.append(model_score)
        print(f"Model {i}: Score = {model_score}, Time = {time.time() - t1:.2f} seconds")
    
    model_to_save= scores_list.index(max(scores_list))
    
    save_best_model(models_list[model_to_save])
    
    print("modelo guardado")
    print(scores_list,max(scores_list),np.mean(scores_list) )
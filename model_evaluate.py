import numpy as np

def wer(ref, hyp):
    """
    Calculate the word error rate (WER).
    WER is defined as the number of substitutions, deletions, and insertions
    divided by the number of words in the reference.
    """
    r = ref.split()
    h = hyp.split()
    d = np.zeros((len(r)+1)*(len(h)+1), dtype=np.uint8)
    d = d.reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion = d[i][j-1] + 1
                deletion = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)
    
    if len(r) == 0:
        return float('inf')  # To handle division by zero if reference is empty
    
    return d[len(r)][len(h)] / float(len(r))

def sentence_similarity(ref, hyp):
    """
    Calculate the sentence similarity percentage.
    """
    r = ref.split()
    h = hyp.split()
    matches = sum(1 for r_word, h_word in zip(r, h) if r_word == h_word)
    return (matches / max(len(r), len(h))) * 100

def ser(ref, hyp):
    """
    Calculate the sentence error rate (SER).
    SER is 1 if the hypothesis does not match the reference exactly, otherwise 0.
    """
    return 1 if ref != hyp else 0

def evaluate_model(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    results = []
    total_wer = 0
    total_similarity = 0
    total_ser = 0
    num_pairs = len(lines) // 2
    
    for i in range(0, len(lines), 2):
        ref = lines[i]
        hyp = lines[i+1]
        
        wer_score = wer(ref, hyp)
        similarity_score = sentence_similarity(ref, hyp)
        ser_score = ser(ref, hyp)
        
        total_wer += wer_score
        total_similarity += similarity_score
        total_ser += ser_score
        
        results.append(f"Reference: {ref}")
        results.append(f"Hypothesis: {hyp}")
        results.append(f"WER: {wer_score:.2f}")
        results.append(f"Similarity: {similarity_score:.2f}%")
        results.append(f"SER: {ser_score}")
        results.append("-" * 30)
    
    avg_wer = total_wer / num_pairs
    avg_similarity = total_similarity / num_pairs
    avg_ser = total_ser / num_pairs
    
    results.append(f"Average WER: {avg_wer:.2f}")
    results.append(f"Average Similarity: {avg_similarity:.2f}%")
    results.append(f"Average SER: {avg_ser:.2f}")
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(results))

# Evaluate the model using the provided file and output to a text file
evaluate_model('C:/Users/lukas/voxforge/acoustic_model/output_file.txt', 'C:/Users/lukas/voxforge/acoustic_model/evaluation_results.txt')

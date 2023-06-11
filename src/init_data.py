import pandas as pd

def load_data():
    df = pd.read_csv('../data/song.csv')
    #曲のリスト
    S = list(df['曲名'].unique())
    #人のリスト
    I = list(df['人'].unique())
    #曲の点数リスト
    V = {(i,s):sc for i,s,sc in zip(df['人'], df['曲名'], df['スコア'])}
    #歌った回数のリスト
    P = {(i,s):sc for i,s,sc in zip(df['人'], df['曲名'], df['歌った回数'])}
    # 全ての人と曲の組み合わせに対して
    for i in I:
        for s in S:
            # もしスコアが存在しなければ、0を設定
            if (i, s) not in V:
                V[(i, s)] = 0
                P[(i, s)] = 0
    #カラオケ最大時間
    T = 60
    #曲の長さ
    t = dict(zip(df['曲名'], df['長さ']))
    #明るさリスト
    b = dict(zip(df["曲名"],df["明るさ"]))
    #共通の曲リスト
    songs_player1 = set(df[df['人'] == 1]['曲名'])
    songs_player2 = set(df[df['人'] == 2]['曲名'])
    C = songs_player1 & songs_player2
    #最大歌う回数
    K = T//df["長さ"].min()
    K = [k for k in range(1,int(K)+1)]
    return S, I, V, P, T, t, b, C, K
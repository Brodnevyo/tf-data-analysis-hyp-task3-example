from scipy import stats


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> bool:
    t_stat, p_value = stats.ttest_1samp(x, 300)
    return (t_stat < 0) and (p_value / 2 < 0.08)

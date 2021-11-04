<details>
    <summary>Hint 1</summary>
    <p>If you know that you can get away with a maximum weight of `w`, what do we know about other possible weights?</p>
</details>

<details>
    <summary>Hint 2</summary>
    <p>If we can divvy out the items between the boxes such that the heaviest box has weight `w`, then the answer is no higher than `w`.</p>
</details>

<details>
    <summary>Hint 3</summary>
    <p>We can binary search for the answer `w`: if we can spread out the items such that the heaviest box is no heavier than `x`, then the answer `w <= x`.</p>
</details>
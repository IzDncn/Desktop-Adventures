namespace DesktopAdventures;

public enum CharacterState
{
    Idle,
    Reacting
}

/// <summary>Ein Lagerfeuer-Charakter mit kleiner Zustandsmaschine (Idle / Reacting).</summary>
public sealed class Character
{
    private readonly AnimatedSprite _sprite;
    private readonly Animation _idle;
    private readonly Animation _react;
    private readonly string[] _lines;
    private readonly Random _rng = new();

    public string Name { get; }
    public CharacterState State { get; private set; } = CharacterState.Idle;

    /// <summary>Wird ausgeloest, wenn der Charakter etwas sagt (Sprechblase).</summary>
    public event Action<string>? Said;

    public Character(string name, AnimatedSprite sprite, Animation idle, Animation react, string[] lines)
    {
        Name = name;
        _sprite = sprite;
        _idle = idle;
        _react = react;
        _lines = lines;

        _sprite.Finished += OnReactFinished;
        _sprite.Play(_idle);
    }

    public void OnClicked()
    {
        if (State == CharacterState.Reacting) return;

        State = CharacterState.Reacting;
        _sprite.Play(_react);
        Said?.Invoke(_lines[_rng.Next(_lines.Length)]);
    }

    private void OnReactFinished()
    {
        State = CharacterState.Idle;
        _sprite.Play(_idle);
    }
}

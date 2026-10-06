using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Threading;

namespace Lagerfeuer;

public partial class MainWindow : Window
{
    private const int Scale = 5;          // 1 Sprite-Pixel = 5 Bildschirm-Pixel
    private const int ScreenMargin = 16;  // Abstand zum rechten Bildschirmrand

    private readonly DispatcherTimer _loop = new() { Interval = TimeSpan.FromMilliseconds(33) };
    private readonly DispatcherTimer _bubbleTimer = new() { Interval = TimeSpan.FromSeconds(2.5) };
    private DateTime _lastTick = DateTime.UtcNow;

    private readonly AnimatedSprite _fireSprite;
    private readonly AnimatedSprite _characterSprite;
    private readonly Character _character;

    public MainWindow()
    {
        InitializeComponent();

        // --- Feuer: 16x16, Loop ---
        FireImage.Width = FireImage.Height = 16 * Scale;
        Canvas.SetLeft(FireImage, 150);
        Canvas.SetTop(FireImage, Height - 16 * Scale);
        _fireSprite = new AnimatedSprite(FireImage);
        _fireSprite.Play(Animation.Load("fire.png", 16, 16, 120, loop: true));

        // --- Charakter: 16x24 ---
        CharacterImage.Width = 16 * Scale;
        CharacterImage.Height = 24 * Scale;
        Canvas.SetLeft(CharacterImage, 60);
        Canvas.SetTop(CharacterImage, Height - 24 * Scale);
        _characterSprite = new AnimatedSprite(CharacterImage);

        _character = new Character(
            "Wanderer",
            _characterSprite,
            idle: Animation.Load("char_idle.png", 16, 24, 400, loop: true),
            react: Animation.Load("char_react.png", 16, 24, 150, loop: false),
            lines: new[]
            {
                "Mhm, schoen warm hier.",
                "Hast du Marshmallows dabei?",
                "Das Feuer knistert so gemuetlich...",
                "Noch ein Scheit, dann geht's los!"
            });
        _character.Said += ShowBubble;

        // --- Bubble ---
        Canvas.SetLeft(Bubble, 10);
        Canvas.SetTop(Bubble, 8);
        _bubbleTimer.Tick += (_, _) =>
        {
            Bubble.Visibility = Visibility.Collapsed;
            _bubbleTimer.Stop();
        };

        // --- Game-Loop ---
        _loop.Tick += OnTick;
        _loop.Start();
    }

    private void Window_Loaded(object sender, RoutedEventArgs e)
    {
        PlaceAboveTaskbar();
    }

    /// <summary>Setzt das Fenster unten rechts direkt auf die Taskleiste (Arbeitsbereich-Kante).</summary>
    private void PlaceAboveTaskbar()
    {
        var area = SystemParameters.WorkArea; // Bildschirm ohne Taskleiste, in DIPs
        Left = area.Right - Width - ScreenMargin;
        Top = area.Bottom - Height;
    }

    private void OnTick(object? sender, EventArgs e)
    {
        var now = DateTime.UtcNow;
        double dtMs = (now - _lastTick).TotalMilliseconds;
        _lastTick = now;

        _fireSprite.Update(dtMs);
        _characterSprite.Update(dtMs);
    }

    private void ShowBubble(string text)
    {
        BubbleText.Text = text;
        Bubble.Visibility = Visibility.Visible;
        _bubbleTimer.Stop();
        _bubbleTimer.Start();
    }

    private void Character_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
    {
        _character.OnClicked();
    }

    private void Exit_Click(object sender, RoutedEventArgs e)
    {
        Application.Current.Shutdown();
    }
}

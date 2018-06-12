using System.Threading.Tasks;
using Microsoft.Bot;
using Microsoft.Bot.Builder;
using Microsoft.Bot.Builder.Core.Extensions;
using Microsoft.Bot.Schema;
using Microsoft.Bot.Builder.Dialogs;
namespace Bot
{
    public class LuisBot : IBot
    {
        private readonly DialogSet dialogs;
        public LuisBot()
        {
            dialogs = new DialogSet();
            dialogs.Add("None", new WaterfallStep[] { DefaultDialog });
            dialogs.Add("ScoreInquiry", new WaterfallStep[] { AskReminderTitle, SaveReminder });
            dialogs.Add("TitlePrompt", new TextPrompt(TitleValidator));
            dialogs.Add("ShowReminderPrompt", new ChoicePrompt(Culture.English));
        }

        public Task OnTurn(ITurnContext turnContext)
        {
            throw new System.NotImplementedException();
        }

        private Task DefaultDialog(DialogContext dialogContext, object args, SkipStepFunction next)
        {
            return dialogContext.Context.SendActivity("对不起我不理解你在说什么");
        }
    }
}

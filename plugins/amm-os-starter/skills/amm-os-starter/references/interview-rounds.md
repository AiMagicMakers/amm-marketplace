# Interview: 3 rounds

Everything below is meant to be said to the user, in English, addressing them as "you". The bullets are prompts to help them talk, not required questions. The person answers what speaks to them and leaves the rest.

## Welcome message (send before round 1, no tool call)

> Hello {Name}. We are going to build your Second Brain: a folder of simple files where AI finds who you are, what you sell, to whom, and how you write. After that, every time you ask an AI for something, it no longer has to rediscover everything.
>
> There are 3 short steps. In each step, answer however you like:
> - **type** freely, in small pieces or all at once;
> - **dictate**: use the dictation on your phone or computer, talk for 2 to 3 minutes, and paste the text;
> - **paste links** (your website, your Instagram page, an online document);
> - **point to files** (a presentation, a quote template, a sales brief).
>
> There are no wrong answers. If you do not know, skip it: I will write "[TO COMPLETE]" and you can come back later. Never give me a national ID number (CIN), bank details (RIB), passwords or your clients' contact details. To skip all the questions, write "skip".

## If the user gave a starting document (for example a sales brief)

Read it before round 1. Say in one sentence what you took from it. In the rounds, only ask what is missing or unclear, and say so ("I already have your offers in the brief, so I am not asking again").

## Round 1: You and your business

Form title: **You and your business**. Four categories.

**1/12 Who are you?**
- First name, job, city, how long you have been doing this
- Your story in a few sentences: where you come from, why you started this business
- How you would like a friend to introduce you to a future client
- 3 to 5 words that describe you

**2/12 What you sell**
- Your services or products, one sentence each
- Who they are for
- What you do not do (and refuse)
- Since when you have offered them

**3/12 Your offers and prices**
- For each offer: name, what is included, duration or format, price in DH excl. VAT (20% VAT is added on top)
- Entry offers, main offers, subscriptions if any
- Discounts, deposits and payment terms you apply
- If you do not have a fixed price yet, say so: it will be noted as it is

**4/12 Why clients choose you**
- What your clients say about you, in their words if you have them
- What you do better or differently from others
- The objections you hear most often, and what you answer
- One example of a result you obtained, only if it is real

## Round 2: Clients and style

Form title: **Your clients and your style**. Four categories.

**5/12 Your typical client**
- Who they are: job, type of company, size, city
- Their day, their tools, what keeps them busy
- How they find you (word of mouth, Instagram, WhatsApp, recommendation...)
- How long they take to decide
- 2 or 3 typical cases, without names of people (example: "a transport SMB in Casablanca")

**6/12 Their words and their problems**
- The exact sentences they use to describe their problem
- Their 2 or 3 biggest problems
- What pushed them to look for help
- What they want in the end, in their words

**7/12 Your tone**
- How you talk to clients: formal or friendly, direct or warm
- The language you write to your clients in (English, French, Arabic, Darija, or a mix)
- 5 words that describe the way you write
- Phrases you often repeat

**8/12 Forbidden words and texts that sound like you**
- Words, expressions or promises you never want to see in a text written in your name
- Topics you do not talk about in public
- Paste 1 to 3 texts you wrote and liked (a post, a sales message, an email). I will use them as examples

## Round 3: How you work

Form title: **How you work**. Four categories.

**9/12 Your key processes**
- The 2 or 3 things you do again and again: first contact, quote, delivery, invoicing, follow-up
- For each: the main steps, how long it takes, the tool used
- Where it usually happens (WhatsApp, email, phone, on site)

**10/12 Your tools**
- Messaging, email, social networks, calendar
- Quotes and invoicing, accounting, payment
- Client follow-up (notebook, Excel, online tool)
- AI tools you already use
- For each need: where the reference information lives

**11/12 Your projects and goals**
- Current projects: name, goal in one sentence, where it stands, deadline
- Your goals for the year, with a number if you have one, and why they matter
- What you decided not to do this year to stay focused

**12/12 Your "drains" to automate**
- One or two tasks that weigh on you, repetitive, that you would like to hand to AI
- Tell them with this model:
  - **When** something happens (X)
  - **I do** this (Y)
  - **it takes** this much time (Z)
  - **the result** is that (W)
  - **I would like** this instead (V)
- Example of the form: "When a prospect asks for a price on WhatsApp, I rewrite my offer by hand, it takes 20 minutes, the result is a long message, I would like to send a ready-made answer in 2 minutes."

## How to run a round

### In Cowork (tool `mcp__visualize__show_widget` available)

1. Call `mcp__visualize__read_me` once before the first widget, without mentioning it to the user.
2. One widget per round. Technical title: `amm_round_1`, `amm_round_2`, `amm_round_3`. Write the `loading_messages` in English, for example: "Preparing the form", "Just a moment".
3. Each category has two fields: a large text field (free answer, pasted dictation) and a small "Links and files (one per line)" field. The category's bullets appear above, in small text.
4. A "Send" button gathers everything into one text and calls `sendPrompt(...)`. That text comes back as the user's message. An empty category is left out.

Widget template (adapt it, 4 `cat` blocks per round):

```html
<style>
  .amm { font-family: inherit; max-width: 640px; }
  .amm h3 { margin: 0 0 12px; font-size: 16px; font-weight: 600; }
  .amm .cat { margin-bottom: 20px; }
  .amm .cat label { display: block; font-weight: 600; font-size: 14px; margin-bottom: 4px; }
  .amm .cat ul { margin: 4px 0 8px; padding-left: 18px; font-size: 12.5px; color: var(--color-text-secondary); }
  .amm textarea { width: 100%; box-sizing: border-box; border-radius: 10px; padding: 10px; font: inherit; font-size: 13px; border: 1px solid var(--color-border-subtle); margin-bottom: 6px; }
  .amm button { padding: 10px 18px; border-radius: 10px; border: 0; font: inherit; font-weight: 600; cursor: pointer; }
</style>
<form class="amm" onsubmit="return false">
  <h3>You and your business</h3>

  <div class="cat">
    <label>1/12 Who are you?</label>
    <ul><li>First name, job, city, how long</li><li>Your story in a few sentences</li></ul>
    <textarea id="c1" rows="5" placeholder="Type or paste your answer here (you can dictate)"></textarea>
    <textarea id="c1l" rows="2" placeholder="Links and files, one per line (optional)"></textarea>
  </div>

  <!-- Repeat for the 3 other categories of the round, ids c2/c2l, c3/c3l, c4/c4l -->

  <button id="send">Send this round</button>
</form>
<script>
  const titles = {c1:"1/12 Who are you?", c2:"2/12 What you sell", c3:"3/12 Offers and prices", c4:"4/12 Why clients choose you"};
  document.getElementById("send").addEventListener("click", () => {
    let out = "Round 1\n";
    for (const id of Object.keys(titles)) {
      const t = document.getElementById(id).value.trim();
      const l = document.getElementById(id + "l").value.trim();
      if (t || l) out += "\n## " + titles[id] + "\n" + t + (l ? "\nLinks and files:\n" + l : "") + "\n";
    }
    sendPrompt(out);
  });
</script>
```

Adapt the ids and titles to the round (5 to 8 for round 2, 9 to 12 for round 3). No emojis in the widget.

### In Claude Code or any other tool (no widget)

Post the round as a block of text: the round title, then for each category its title and bullets as written above, then one sentence: "Answer however you like, by category or all at once. Write 'next' to skip this round." Wait for the answer before posting the next round. Do not use AskUserQuestion for these rounds: the answers are too long.

## Answers received

- A category with no answer is skipped. Do not ask again.
- If an answer contains a national ID, bank details, a password, or the name, phone or email of a private client, do not write it in any file and say so kindly in one sentence.
- Between rounds, do not comment and do not ask clarifying questions. Read the category's links and files, then move to the next round.

This is a TODO-list web project.

# TDD methodologies
- 编写1个用例-运行测试并按预期失败-编写最少代码实现功能并运行测试直至通过。重复这个步骤，直至没有可写的用例。
- User Story: A description of how the application will work from the point of view of the user. Used to structure a functional test.
- Expected failure: When a test fails in the way that we expected it to.
- TDD and agile software development methodologies often go together, and one of the things we often talk about is the minimum viable app.


# Functional Test == Acceptance Test == End-to-End Test == black box test
- FT(functional test): Tests that use Selenium let us drive a real web browser, so they really let us see how the application functions from the user’s point of view. The main point is that these kinds of tests look at how the whole application functions, from the outside. Another term is black box test, because the test doesn’t know anything about the internals of the system under test. （功能测试是从用户使用角度去验证功能可用。有点类似BDD了）
- FTs should have a human-readable story that we can follow. We make it explicit using comments that accompany the test code. When creating a new FT, we can write the comments first, to capture the key points of the User Story. (在注释中描述功能)
- We’ll see that Django uses them a lot in the files it generates for us to use as a way of suggesting helpful bits of its API. And, of course, we use comments to explain the User Story in our functional tests. (注释的用途。不要去重复代码)
- There’s a principle called Don’t Repeat Yourself (DRY), which we like to apply by following the mantra three strikes and refactor. You can copy and paste code once, and it may be premature to try to remove the duplication it causes, but once you get three occurrences, it’s time to remove duplication.  (DRY)

# Unit Test
- The basic distinction is that functional tests test the application from the outside, from the point of view of the user. Unit tests test the application from the inside, from the point of view of the programmer.
- Unit tests should help us to write code that’s clean and bug free.
- Tests can help us write the correct code, one tiny step at a time.


# Work flow
workflow will look a bit like this:

We start by writing a functional test, describing the new functionality from the user’s point of view.

Once we have a functional test that fails, we start to think about how to write code that can get it to pass (or at least to get past its current failure). We now use one or more unit tests to define how we want our code to behave—​the idea is that each line of production code we write should be tested by (at least) one of our unit tests.

Once we have a failing unit test, we write the smallest amount of application code we can, just enough to get the unit test to pass. We may iterate between steps 2 and 3 a few times, until we think the functional test will get a little further.

Now we can rerun our functional tests and see if they pass, or get a little further. That may prompt us to write some new unit tests, and some new code, and so on.